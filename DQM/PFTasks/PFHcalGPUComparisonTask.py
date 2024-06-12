import FWCore.ParameterSet.Config as cms

def PFHcalGPUComparisonTask(**kwargs):
  mod = cms.EDProducer('PFHcalGPUComparisonTask',
    name = cms.untracked.string('pfCaloGPUCompDir'),
    pfClusterToken_ref = cms.untracked.InputTag('hltParticleFlowClusterHCALSerialSync'),
    pfClusterToken_target = cms.untracked.InputTag('hltParticleFlowClusterHCAL'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
