import FWCore.ParameterSet.Config as cms

def CSCMonitorModule(**kwargs):
  mod = cms.EDProducer('CSCMonitorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
