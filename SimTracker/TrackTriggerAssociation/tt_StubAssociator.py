import FWCore.ParameterSet.Config as cms

def tt_StubAssociator(**kwargs):
  mod = cms.EDProducer('tt::StubAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
