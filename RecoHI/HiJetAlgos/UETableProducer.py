import FWCore.ParameterSet.Config as cms

def UETableProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('UETableProducer',
    txtFile = cms.string('example'),
    debug = cms.untracked.bool(False),
    jetCorrectorFormat = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
