import FWCore.ParameterSet.Config as cms

def HLT2L1P2GTCandL1P2GTCandDZ(*args, **kwargs):
  mod = cms.EDFilter('HLT2L1P2GTCandL1P2GTCandDZ',
    saveTags = cms.bool(True),
    originTag1 = cms.VInputTag('hltOriginal1'),
    originTag2 = cms.VInputTag('hltOriginal2'),
    l1GTAlgoBlockTag = cms.InputTag('l1tGTAlgoBlockProducer'),
    l1GTAlgoName1 = cms.string(''),
    l1GTAlgoName2 = cms.string(''),
    triggerType1 = cms.int32(0),
    triggerType2 = cms.int32(0),
    MinDR = cms.double(-1),
    MaxDZ = cms.double(0.2),
    MinPixHitsForDZ = cms.int32(0),
    checkSC = cms.bool(False),
    MinN = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
