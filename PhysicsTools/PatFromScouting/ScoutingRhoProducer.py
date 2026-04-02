import FWCore.ParameterSet.Config as cms

def ScoutingRhoProducer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingRhoProducer',
    src = cms.InputTag('hltScoutingPFPacker', 'rho'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
