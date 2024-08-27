import FWCore.ParameterSet.Config as cms

def CTPPSCompositeESSource(**kwargs):
  mod = cms.ESSource('CTPPSCompositeESSource',
    compactViewTag = cms.string(''),
    lhcInfoLabel = cms.string(''),
    opticsLabel = cms.string(''),
    seed = cms.uint32(1),
    isRun2 = cms.bool(False),
    generateEveryNEvents = cms.untracked.uint32(1),
    verbosity = cms.untracked.uint32(0),
    periods = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
