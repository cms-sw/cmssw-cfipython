import FWCore.ParameterSet.Config as cms

def HLTEgammaCombMassFilter(**kwargs):
  mod = cms.EDFilter('HLTEgammaCombMassFilter',
    saveTags = cms.bool(True),
    firstLegLastFilter = cms.InputTag('firstFilter'),
    secondLegLastFilter = cms.InputTag('secondFilter'),
    minMass = cms.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
