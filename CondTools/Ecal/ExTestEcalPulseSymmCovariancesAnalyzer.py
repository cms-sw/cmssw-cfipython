import FWCore.ParameterSet.Config as cms

def ExTestEcalPulseSymmCovariancesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalPulseSymmCovariancesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
