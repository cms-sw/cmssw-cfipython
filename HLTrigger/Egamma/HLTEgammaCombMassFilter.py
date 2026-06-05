import FWCore.ParameterSet.Config as cms

def HLTEgammaCombMassFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTEgammaCombMassFilter',
    saveTags = cms.bool(True),
    firstLegLastFilter = cms.InputTag('firstFilter'),
    secondLegLastFilter = cms.InputTag('secondFilter'),
    l1EGCand = cms.InputTag('hltEgammaCandidates'),
    minMass = cms.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
