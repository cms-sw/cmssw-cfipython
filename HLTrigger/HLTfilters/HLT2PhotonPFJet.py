import FWCore.ParameterSet.Config as cms

def HLT2PhotonPFJet(**kwargs):
  mod = cms.EDFilter('HLT2PhotonPFJet',
    saveTags = cms.bool(True),
    originTag1 = cms.VInputTag('hltOriginal1'),
    originTag2 = cms.VInputTag('hltOriginal2'),
    inputTag1 = cms.InputTag('hltFiltered1'),
    inputTag2 = cms.InputTag('hltFiltered22'),
    triggerType1 = cms.int32(0),
    triggerType2 = cms.int32(0),
    MinDeta = cms.double(1),
    MaxDeta = cms.double(-1),
    MinDphi = cms.double(1),
    MaxDphi = cms.double(-1),
    MinDelR = cms.double(1),
    MaxDelR = cms.double(-1),
    MinPt = cms.double(1),
    MaxPt = cms.double(-1),
    MinMinv = cms.double(1),
    MaxMinv = cms.double(-1),
    MinN = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod