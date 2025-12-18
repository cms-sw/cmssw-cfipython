import FWCore.ParameterSet.Config as cms

def QIE11Task(*args, **kwargs):
  mod = cms.EDProducer('QIE11Task',
    subsystem = cms.untracked.string('Hcal'),
    mtype = cms.untracked.bool(True),
    ptype = cms.untracked.int32(0),
    maxLS = cms.untracked.int32(4000),
    tagRaw = cms.untracked.InputTag('rawDataCollector'),
    name = cms.untracked.string('QIE11Task'),
    debug = cms.untracked.int32(0),
    runkeyVal = cms.untracked.int32(0),
    runkeyName = cms.untracked.string('pp_run'),
    tagQIE11 = cms.untracked.InputTag('hcalDigis'),
    cut = cms.untracked.double(20),
    ped = cms.untracked.int32(4),
    laserType = cms.untracked.int32(-1),
    eventType = cms.untracked.int32(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
