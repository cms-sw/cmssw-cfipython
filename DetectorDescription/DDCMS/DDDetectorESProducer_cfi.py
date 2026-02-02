import FWCore.ParameterSet.Config as cms

from .DDDetectorESProducer import DDDetectorESProducer

DDDetectorESProducer = DDDetectorESProducer(
  rootDDName = 'cms:OCMS',
  label = '',
  fromDB = False,
  appendToDataLabel = ''
)
