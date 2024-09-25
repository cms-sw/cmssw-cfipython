import FWCore.ParameterSet.Config as cms

def MillePedeFileConverter(*args, **kwargs):
  mod = cms.EDProducer('MillePedeFileConverter',
    fileDir = cms.string(''),
    inputBinaryFile = cms.string('milleBinary.dat'),
    fileBlobLabel = cms.string('milleBinary.dat'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
