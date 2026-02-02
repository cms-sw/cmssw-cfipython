import FWCore.ParameterSet.Config as cms

from .DDDetectorESProducer import DDDetectorESProducer

DDDetectorESProducerFromDB = DDDetectorESProducer(
  rootDDName = 'cms:OCMS',
  label = 'Extended',
  fromDB = True,
  appendToDataLabel = ''
)
