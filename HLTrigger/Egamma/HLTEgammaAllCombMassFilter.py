import FWCore.ParameterSet.Config as cms

def HLTEgammaAllCombMassFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTEgammaAllCombMassFilter',
    saveTags = cms.bool(True),
    firstLegLastFilter = cms.InputTag('firstFilter'),
    secondLegLastFilter = cms.InputTag('secondFilter'),
    minMass = cms.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
