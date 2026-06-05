import FWCore.ParameterSet.Config as cms

def CSCTFUnpacker(*args, **kwargs):
  mod = cms.EDProducer('CSCTFUnpacker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
