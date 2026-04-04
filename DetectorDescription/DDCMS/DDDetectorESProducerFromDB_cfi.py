import FWCore.ParameterSet.Config as cms

from .DDDetectorESProducer import DDDetectorESProducer

DDDetectorESProducerFromDB = DDDetectorESProducer(

  fromDB = True,
  label = 'Extended'
)
