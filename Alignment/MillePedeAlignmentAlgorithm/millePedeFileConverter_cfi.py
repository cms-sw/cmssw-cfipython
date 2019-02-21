import FWCore.ParameterSet.Config as cms

millePedeFileConverter = cms.EDProducer('MillePedeFileConverter',
  fileDir = cms.string(''),
  inputBinaryFile = cms.string('milleBinary.dat'),
  fileBlobLabel = cms.string('milleBinary.dat')
)
