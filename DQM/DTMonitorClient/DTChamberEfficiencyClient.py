import FWCore.ParameterSet.Config as cms

def DTChamberEfficiencyClient(*args, **kwargs):
  mod = cms.EDProducer('DTChamberEfficiencyClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
