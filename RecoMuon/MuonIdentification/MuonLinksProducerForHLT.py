import FWCore.ParameterSet.Config as cms

def MuonLinksProducerForHLT(*args, **kwargs):
  mod = cms.EDProducer('MuonLinksProducerForHLT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
