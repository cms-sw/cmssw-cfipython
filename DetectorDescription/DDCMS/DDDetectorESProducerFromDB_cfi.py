import FWCore.ParameterSet.Config as cms

DDDetectorESProducerFromDB = cms.ESSource('DDDetectorESProducer',
  rootDDName = cms.string('cms:OCMS'),
  label = cms.string('Extended'),
  fromDB = cms.bool(True),
  appendToDataLabel = cms.string('')
)
