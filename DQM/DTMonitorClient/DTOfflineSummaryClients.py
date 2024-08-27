import FWCore.ParameterSet.Config as cms

def DTOfflineSummaryClients(**kwargs):
  mod = cms.EDProducer('DTOfflineSummaryClients',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
