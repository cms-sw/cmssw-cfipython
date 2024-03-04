import FWCore.ParameterSet.Config as cms

def PFJetsMaxInvMassModule(**kwargs):
  mod = cms.EDProducer('PFJetsMaxInvMassModule',
    PFJetSrc = cms.InputTag(''),
    maxInvMassPairOnly = cms.bool(True),
    removeMaxInvMassPair = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
