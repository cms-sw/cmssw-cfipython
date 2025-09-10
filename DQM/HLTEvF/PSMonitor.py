import FWCore.ParameterSet.Config as cms

def PSMonitor(*args, **kwargs):
  mod = cms.EDProducer('PSMonitor',
    ugtBXInputTag = cms.InputTag('hltGtStage2Digis'),
    folderName = cms.string('HLT/PSMonitoring'),
    histoPSet = cms.PSet(
      psColumnPSet = cms.PSet(
        nbins = cms.int32(8)
      ),
      lsPSet = cms.PSet(
        nbins = cms.int32(2500)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
