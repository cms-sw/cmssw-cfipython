import FWCore.ParameterSet.Config as cms

def GenHDF5Producer(*args, **kwargs):
  mod = cms.EDProducer('GenHDF5Producer',
    fileName = cms.string('gen.h5'),
    blockRows = cms.untracked.uint32(0),
    maxCachedBlocks = cms.untracked.uint32(4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
