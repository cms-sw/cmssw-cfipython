import FWCore.ParameterSet.Config as cms

hcalGPUComparisonTask = cms.EDProducer('HcalGPUComparisonTask',
  name = cms.untracked.string('HcalGPUComparisonTask'),
  debug = cms.untracked.int32(0),
  runkeyVal = cms.untracked.int32(0),
  runkeyName = cms.untracked.string('pp_run'),
  ptype = cms.untracked.int32(1),
  mtype = cms.untracked.bool(True),
  subsystem = cms.untracked.string('Hcal'),
  tagHBHE_ref = cms.untracked.InputTag('hbhereco@cpu'),
  tagHBHE_target = cms.untracked.InputTag('hbhereco@cuda'),
  tagRaw = cms.untracked.InputTag('rawDataCollector'),
  mightGet = cms.optional.untracked.vstring
)
