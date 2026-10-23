import FWCore.ParameterSet.Config as cms

def HLTPrescaleRecorder(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
