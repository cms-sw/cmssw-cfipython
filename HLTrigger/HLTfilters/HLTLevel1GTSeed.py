import FWCore.ParameterSet.Config as cms

def HLTLevel1GTSeed(**kwargs):
  mod = cms.EDFilter('HLTLevel1GTSeed',
    saveTags = cms.bool(True),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    L1NrBxInEvent = cms.int32(3),
    L1TechTriggerSeeding = cms.bool(False),
    L1UseAliasesForSeeding = cms.bool(True),
    L1SeedsLogicalExpression = cms.string(''),
    L1GtReadoutRecordTag = cms.InputTag('gtDigis'),
    L1GtObjectMapTag = cms.InputTag('l1GtObjectMap'),
    L1CollectionsTag = cms.InputTag('l1extraParticles'),
    L1MuonCollectionTag = cms.InputTag('l1extraParticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
