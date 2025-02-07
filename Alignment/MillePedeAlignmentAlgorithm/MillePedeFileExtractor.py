import FWCore.ParameterSet.Config as cms

def MillePedeFileExtractor(*args, **kwargs):
  mod = cms.EDAnalyzer('MillePedeFileExtractor',
    fileDir = cms.string(''),
    outputBinaryFile = cms.string('milleBinary%04d.dat'),
    fileBlobInputTag = cms.InputTag('millePedeFileConverter'),
    maxNumberOfBinaries = cms.int32(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
