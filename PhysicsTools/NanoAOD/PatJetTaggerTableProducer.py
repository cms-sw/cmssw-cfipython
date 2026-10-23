import FWCore.ParameterSet.Config as cms

def PatJetTaggerTableProducer(*args, **kwargs):
  mod = cms.EDProducer('PatJetTaggerTableProducer',
    nameDeepJet = cms.string('Jet'),
    idx_nameDeepJet = cms.string('djIdx'),
    n_cpf = cms.uint32(2),
    n_npf = cms.uint32(2),
    n_sv = cms.uint32(2),
    n_lt = cms.uint32(2),
    jets = cms.InputTag('slimmedJetsPuppi'),
    tagInfo_src = cms.InputTag('pfUnifiedParticleTransformerAK4TagInfosPuppiWithDeepInfo'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
