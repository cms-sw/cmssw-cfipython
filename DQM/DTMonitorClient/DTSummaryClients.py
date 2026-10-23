import FWCore.ParameterSet.Config as cms

def DTSummaryClients(*args, **kwargs):
  mod = cms.EDProducer('DTSummaryClients',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
