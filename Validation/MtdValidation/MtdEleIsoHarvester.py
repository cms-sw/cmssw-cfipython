import FWCore.ParameterSet.Config as cms

def MtdEleIsoHarvester(*args, **kwargs):
  mod = cms.EDProducer('MtdEleIsoHarvester',
    folder = cms.string('MTD/ElectronIso/'),
    option_plots = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
