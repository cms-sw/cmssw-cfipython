import FWCore.ParameterSet.Config as cms

def tt_StubAssociator(*args, **kwargs):
  mod = cms.EDProducer('tt::StubAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
