import FWCore.ParameterSet.Config as cms

millePedeFileExtractor = cms.EDAnalyzer('MillePedeFileExtractor',
  fileDir = cms.string(''),
  outputBinaryFile = cms.string('milleBinary%04d.dat'),
  fileBlobInputTag = cms.InputTag('millePedeFileConverter'),
  maxNumberOfBinaries = cms.int32(1000)
)
