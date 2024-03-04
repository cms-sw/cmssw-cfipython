import FWCore.ParameterSet.Config as cms

def MillePedeFileConverter(**kwargs):
  mod = cms.EDProducer('MillePedeFileConverter',
    fileDir = cms.string(''),
    inputBinaryFile = cms.string('milleBinary.dat'),
    fileBlobLabel = cms.string('milleBinary.dat'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
