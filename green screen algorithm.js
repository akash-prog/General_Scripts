var fgImage = new SimpleImage(//"image source");

var bgimage = new SimpleImage(//"image source");

var output = new SimpleImage(fgImage.getwidth(), fgImage.getHeight());

for (var pixel of fgImage.values()) {

if (pixel.getGreen() > pixel.getRed() + pixel.getBlue()){

    var x = pixel.getX();
    var y = pixel.getY();
    var bgPixel = bgImage.getPixel(x,y);


output.setPixel(x,y, bgPixel);
}

else{
	output.setPixel(pixel.getX(), pixel.getY(), pixel);

}

}

print(output);
