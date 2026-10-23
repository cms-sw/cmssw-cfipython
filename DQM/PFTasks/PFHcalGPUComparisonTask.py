import FWCore.ParameterSet.Config as cms

def PFHcalGPUComparisonTask(*args, **kwargs):
  mod = cms.EDProducer('PFHcalGPUComparisonTask',
    subsystem = cms.untracked.string('ParticleFlow'),
    name = cms.untracked.string('ParticleFlow/pfCaloGPUCompDir'),
    pfClusterToken_ref = cms.untracked.InputTag('hltParticleFlowClusterHCALSerialSync'),
    pfClusterToken_target = cms.untracked.InputTag('hltParticleFlowClusterHCAL'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
