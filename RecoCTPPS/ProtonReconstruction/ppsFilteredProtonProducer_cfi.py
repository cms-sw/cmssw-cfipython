import FWCore.ParameterSet.Config as cms

ppsFilteredProtonProducer = cms.EDProducer('PPSFilteredProtonProducer',
  verbosity = cms.untracked.bool(False),
  tracks_all = cms.PSet(
    local_angle_x_max = cms.double(0.02),
    local_angle_y_max = cms.double(0.02)
  ),
  tracks_pixel = cms.PSet(
    forbidden_RecoInfo_values = cms.vuint32(
      1,
      3
    ),
    number_of_hits_min = cms.uint32(0),
    normalised_chi_sq_max = cms.double(1e+100)
  ),
  protons_single_rp = cms.PSet(
    include = cms.bool(True),
    input_tag = cms.InputTag('ctppsProtons', 'singleRP'),
    output_label = cms.string('singleRP')
  ),
  protons_multi_rp = cms.PSet(
    include = cms.bool(True),
    input_tag = cms.InputTag('ctppsProtons', 'multiRP'),
    output_label = cms.string('multiRP'),
    check_valid_fit = cms.bool(True),
    chi_sq_max = cms.double(0.0001),
    normalised_chi_sq_max = cms.double(1e+100)
  )
)
