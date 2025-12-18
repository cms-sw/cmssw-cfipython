import FWCore.ParameterSet.Config as cms

def HLT3DoublePFJetPhoton(*args, **kwargs):
  mod = cms.EDFilter('HLT3DoublePFJetPhoton',
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
    MinDphi = cms.double(1),
    MaxDphi = cms.double(-1),
    MinDeta = cms.double(1),
    MaxDeta = cms.double(-1),
    MinMinv = cms.double(1),
    MaxMinv = cms.double(-1),
    MinDelR = cms.double(1),
    MaxDelR = cms.double(-1),
    MinPt = cms.double(1),
    MaxPt = cms.double(-1),
    MinN = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
