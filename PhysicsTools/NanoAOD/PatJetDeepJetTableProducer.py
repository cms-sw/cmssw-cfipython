import FWCore.ParameterSet.Config as cms

def PatJetDeepJetTableProducer(**kwargs):
  mod = cms.EDProducer('PatJetDeepJetTableProducer',
    nameDeepJet = cms.string('Jet'),
    idx_nameDeepJet = cms.string('djIdx'),
    n_cpf = cms.uint32(3),
    n_npf = cms.uint32(3),
    n_sv = cms.uint32(4),
    jets = cms.InputTag('slimmedJetsPuppi'),
    tagInfo_src = cms.InputTag('pfDeepFlavourTagInfosPuppiWithDeepInfo'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
