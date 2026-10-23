import FWCore.ParameterSet.Config as cms

def PFJetsMaxInvMassModule(*args, **kwargs):
  mod = cms.EDProducer('PFJetsMaxInvMassModule',
    PFJetSrc = cms.InputTag(''),
    maxInvMassPairOnly = cms.bool(True),
    removeMaxInvMassPair = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
