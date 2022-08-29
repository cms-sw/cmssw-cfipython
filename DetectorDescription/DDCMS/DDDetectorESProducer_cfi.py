import FWCore.ParameterSet.Config as cms

DDDetectorESProducer = cms.ESSource('DDDetectorESProducer',
  confGeomXMLFiles = cms.optional.FileInPath,
  rootDDName = cms.string('cms:OCMS'),
  label = cms.string(''),
  fromDB = cms.bool(False),
  appendToDataLabel = cms.string('')
)
