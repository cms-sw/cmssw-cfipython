import FWCore.ParameterSet.Config as cms

def MillePedeFileExtractor(**kwargs):
  mod = cms.EDAnalyzer('MillePedeFileExtractor',
    fileDir = cms.string(''),
    outputBinaryFile = cms.string('milleBinary%04d.dat'),
    fileBlobInputTag = cms.InputTag('millePedeFileConverter'),
    maxNumberOfBinaries = cms.int32(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
