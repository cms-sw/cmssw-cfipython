import FWCore.ParameterSet.Config as cms

def CTPPSLHCInfoPlotter(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSLHCInfoPlotter',
    lhcInfoLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False),
    outputFile = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
