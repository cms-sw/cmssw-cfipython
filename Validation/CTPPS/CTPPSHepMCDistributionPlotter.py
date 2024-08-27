import FWCore.ParameterSet.Config as cms

def CTPPSHepMCDistributionPlotter(**kwargs):
  mod = cms.EDAnalyzer('CTPPSHepMCDistributionPlotter',
    lhcInfoLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False),
    outputFile = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
