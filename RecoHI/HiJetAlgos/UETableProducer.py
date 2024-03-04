import FWCore.ParameterSet.Config as cms

def UETableProducer(**kwargs):
  mod = cms.EDAnalyzer('UETableProducer',
    txtFile = cms.string('example'),
    debug = cms.untracked.bool(False),
    jetCorrectorFormat = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
