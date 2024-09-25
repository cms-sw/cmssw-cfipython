import FWCore.ParameterSet.Config as cms

def HLT3MuonMuonPhotonMass(*args, **kwargs):
  mod = cms.EDFilter('HLT3MuonMuonPhotonMass',
    saveTags = cms.bool(True),
    originTag1 = cms.VInputTag('hltOriginal1'),
    originTag2 = cms.VInputTag('hltOriginal2'),
    originTag3 = cms.VInputTag('hltOriginal3'),
    inputTag1 = cms.InputTag('hltFiltered1'),
    inputTag2 = cms.InputTag('hltFiltered2'),
    inputTag3 = cms.InputTag('hltFiltered3'),
    triggerType1 = cms.int32(0),
    triggerType2 = cms.int32(0),
    triggerType3 = cms.int32(0),
    MinInvMass = cms.vdouble(0),
    MaxInvMass = cms.vdouble(1000000000000),
    MaxDR = cms.double(10000),
    MinN = cms.int32(0),
    is1and2Same = cms.bool(False),
    is2and3Same = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
