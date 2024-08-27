import FWCore.ParameterSet.Config as cms

def HLTPrescaleRecorder(**kwargs):
  mod = cms.EDProducer('HLTPrescaleRecorder',
    src = cms.int32(0),
    run = cms.bool(True),
    lumi = cms.bool(True),
    event = cms.bool(True),
    condDB = cms.bool(True),
    psetName = cms.string(''),
    hltInputTag = cms.InputTag(''),
    hltDBTag = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
