import FWCore.ParameterSet.Config as cms

def PFRecHitFlatTableProducer(*args, **kwargs):
  mod = cms.EDProducer('PFRecHitFlatTableProducer',
    objName = cms.string('pfrechits'),
    label_rechits = cms.VInputTag(
      'hltParticleFlowRecHitECALUnseeded::HLT',
      'hltParticleFlowRecHitHBHE::HLT',
      'hltParticleFlowRecHitHF::HLT',
      'hltParticleFlowRecHitHO::HLT'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
