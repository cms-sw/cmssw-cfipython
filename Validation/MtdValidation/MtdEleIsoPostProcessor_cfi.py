import FWCore.ParameterSet.Config as cms

MtdEleIsoPostProcessor = cms.EDProducer('MtdEleIsoHarvester',
  folder = cms.string('MTD/ElectronIso/'),
  option_plots = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
