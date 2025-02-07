import FWCore.ParameterSet.Config as cms

def CSCTFPacker(*args, **kwargs):
  mod = cms.EDProducer('CSCTFPacker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
