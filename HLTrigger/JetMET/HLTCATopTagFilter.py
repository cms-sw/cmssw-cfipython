import FWCore.ParameterSet.Config as cms

def HLTCATopTagFilter(**kwargs):
  mod = cms.EDFilter('HLTCATopTagFilter',
    saveTags = cms.bool(True),
    TopMass = cms.double(171),
    maxTopMass = cms.double(230),
    minTopMass = cms.double(140),
    minMinMass = cms.double(50),
    src = cms.InputTag('hltParticleFlow'),
    pfsrc = cms.InputTag('selectedPFJets'),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
