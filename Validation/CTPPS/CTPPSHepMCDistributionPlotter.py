import FWCore.ParameterSet.Config as cms

def CTPPSHepMCDistributionPlotter(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSHepMCDistributionPlotter',
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
